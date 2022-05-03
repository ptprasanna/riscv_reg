from ast import Pass
from logging import warning
import subprocess
import threading
import click
import os
import pandas as pds
import ruamel.yaml
import git
from . import log
from xml.dom import minidom
from urllib.request import urlopen
import datetime
from dateutil import parser

@click.command()
@click.option('--verbose', '-v', default='error', help='Set verbose level', type=click.Choice(['info','error','debug'],case_sensitive=False))
@click.option('--runmanager', '-r', default=False, help='Path of the csv file', type=click.Path(exists=True,resolve_path=True,readable=True))
def cli(verbose,runmanager):
    global logger
    logger = log.logger
    logger.level(verbose)
    data= pds.read_csv(runmanager)
    yaml = ruamel.yaml.YAML()
    with open("riscv_reg.yaml") as file:
        properties = yaml.load(file)
    logger.info(properties.get('CTG_PATH'))

    FOLD_REP = properties.get('FOLD_REP')
    DATASET = properties.get('DATASET')
    CTG_REPO = properties.get('CTG_REPO')
    ISAC_REPO = properties.get('ISAC_REPO')

    logger.info(folderCleanup(FOLD_REP))
    url_Str = properties.get('CTG_PATH')
    with urlopen(url_Str) as com_his:
        xml_str = com_his.read()
    doc = minidom.parseString(xml_str)
    commitDate = doc.getElementsByTagName("updated")[0].firstChild.nodeValue
    lastCommitDate = parser.parse(commitDate)
    lastCommitDate = datetime.datetime.strptime(str(lastCommitDate).split("+")[0],"%Y-%m-%d %H:%M:%S")
    logger.info("The Last commit Date of CTG")
    logger.info(lastCommitDate)
    com_his.close()


    lastRanDate = datetime.datetime.strptime(str(properties.get('CTG_COM')),"%Y-%m-%d %H:%M:%S")
    logger.info("The Last Ran Date of CTG")
    logger.info(lastRanDate)
    if lastRanDate<lastCommitDate:
        ctgFlag = True
        properties['CTG_COM'] = lastCommitDate
        with open("riscv_reg.yaml","w") as file:
            yaml.dump(properties, file)
            file.close()
    else:
        ctgFlag = False
    
    gitVerify(CTG_REPO,ctgFlag)

    logger.info("CTG Flag has been set")
    logger.info(ctgFlag)

    url_Str = properties.get('ISAC_PATH')
    with urlopen(url_Str) as com_his:
        xml_str = com_his.read()
    doc = minidom.parseString(xml_str)
    commitDate = doc.getElementsByTagName("updated")[0].firstChild.nodeValue
    lastCommitDate = parser.parse(commitDate)
    lastCommitDate = datetime.datetime.strptime(str(lastCommitDate).split("+")[0],"%Y-%m-%d %H:%M:%S")
    logger.info("The Last commit Date of ISAC")
    logger.info(lastCommitDate)
    com_his.close()

    lastRanDate = datetime.datetime.strptime(str(properties.get('ISAC_COM')),"%Y-%m-%d %H:%M:%S")
    logger.info("The Last Ran Date of ISAC")
    logger.info(lastRanDate)
    if lastRanDate<lastCommitDate:
        isacFlag = True
        properties['ISAC_COM'] = lastCommitDate
        with open("riscv_reg.yaml","w") as file:
            yaml.dump(properties, file)
            file.close()
    else:
        isacFlag = False
    
    gitVerify(ISAC_REPO,isacFlag)
    
    logger.info("ISAC Flag has been set")
    logger.info(isacFlag)


    isacFlag = True
    if isacFlag or ctgFlag:

        reportpath = datetime.datetime.now()
        reportpath = str(reportpath).replace(" ","_")
        os.mkdir("{0}/{1}".format(FOLD_REP,reportpath))
        
        if os.path.exists(DATASET):
            pass
        else:
            logger.error("Given dataSet path is not correct")
            logger.error(DATASET)
        htmlReport = pds.DataFrame({"Extension":['_'],"Instruction":['_'],"Model":['_'],"Cover%":['_'],"CoverPoints":['_']})
        
        for row in range (data.__len__()):
            ''' This loop iterate through each row of the runmanager and start running it '''
            reports = "{0}/{1}".format(FOLD_REP,reportpath)
            cmdStr = "cd "
            if data.__getitem__("selectTest")[row]:
                            
                model = subprocess.getstatusoutput(f'which '+data.__getitem__("model")[row])
                if model[1]:
                    logger.info("Running on model:")
                    logger.info(data.__getitem__("model")[row])
                else:
                    logger.error("Given model is not available on this machine, Please correct the runmanager")
                    logger.error(data.__getitem__("model")[row])
                    continue
                fl = data.__getitem__("floatLength")[row]
                extension = data.__getitem__("extension")[row].lower()
                cgfPath = '{0}{1}_{2}.cgf'.format(data.__getitem__("cgfPath")[row],extension,data.__getitem__("cgfFile")[row].lower())
                if os.path.exists(cgfPath):
                    logger.info(cgfPath)
                else:
                    logger.error("There is no Such a CGF file Exists, Please correct the runmanager")
                    logger.error(cgfPath)
                    continue

                configPath = '{0}config.ini'.format(data.__getitem__("configPath")[row])
                if os.path.exists(configPath):
                    logger.info(configPath)
                else:
                    logger.error("There is no config.ini file Exists, Please update the runmanager with correct configuration path")
                    logger.error(configPath)
                    continue
                if '32' in extension:
                    bi = 'rv32i'
                else:
                    bi = 'rv64i'
                foldName = extension+"_"+data.__getitem__("cgfFile")[row]
                os.mkdir("{0}/{1}".format(reports,foldName))
                reports = "{0}/{1}".format(reports,foldName)
                cmdStr = cmdStr + reports+";"
                cmdStr = cmdStr + "riscv_ctg -v debug -d tests -r -cf {0} -cf {1} -bi {2} -p 12;riscof -v debug coverage --suite tests --env tests/env --config {5} --no-browser --work-dir work -f {3} -c {4} -c {6}".format(DATASET,cgfPath,bi,fl,DATASET,configPath,cgfPath)
                logger.info(cmdStr)
                
                if os.path.exists(reports):
                    pass
                else:
                    logger.error("Given folder work path is not correct")
                    logger.error(FOLD_REP)

                logPath = reports+"/"+foldName+".log"

                outShellcmd = subprocess.getstatusoutput(cmdStr)

                with open(logPath,"w") as file:
                    log_Str = outShellcmd[1]
                    log_Str = log_Str.replace("[35m","").replace("[0m","").replace("[32m","").replace("[1;31m","")
                    file.write(log_Str)
                    file.close()
                if outShellcmd[0] == 0:
                    logger.info("Run {0} is successfully completed".format(row))
                    tempReport = pds.DataFrame({"Extension":[data.__getitem__("extension")[row]],"Instruction":[data.__getitem__("cgfFile")[row]],"Model":[data.__getitem__("model")[row]],"Cover%":[calculateCoverPercentage(reports,"coverPercent")],"CoverPoints":[calculateCoverPercentage(reports,"coverPoints")]})
                    logger.info(tempReport)
                else:
                    logger.warning("Run {0} is Not completed as expected".format(row))
                    tempReport = pds.DataFrame({"Extension":[data.__getitem__("extension")[row]],"Instruction":[data.__getitem__("cgfFile")[row]],"Model":[data.__getitem__("model")[row]],"Cover%":[0],"CoverPoints":[0]})
                logger.info(outShellcmd[0])
                htmlReport = htmlReport.append(tempReport, ignore_index = True)
                logger.info(htmlReport)
            else:
                continue
    else:
        logger.warning("There isn't any change from the last regression run, hence no run is scheduled")

    htmlReport.to_html(reports+"/riscv_reg_status.html")
# def generateReport(csvData):
#     logger.info("Report Generated")

def calculateCoverPercentage(path,instr):
    with open(path+"/work/suite_coverage.rpt","r") as file:
        lines = file.readlines()
        passCP = 0
        totalCP = 0
        for line in lines:
            if line.find("total_coverage") != -1:
                tmpPStr = int(line.split(':')[1].split('/')[0])
                tmpTStr = int(line.split(':')[1].split('/')[1])
                passCP += tmpPStr
                totalCP += tmpTStr
    file.close()
    if instr=="coverPoints":
        return (str(passCP)+"/"+str(totalCP))
    elif instr=="coverPercent":
        return str(float(passCP*(100/totalCP)))

def folderCleanup(fold_path):
    '''This function is to keep the last 30 report folders and to delete the rest'''
    cmdStr = "cd "+fold_path+";"+"find * -maxdepth 0 -type d | sort -nr | awk 'NR > 30 {print $0}' | xargs rm -rf"
    cleanStatus = subprocess.getstatusoutput(cmdStr)
    if cleanStatus[0]==0:
        return("Cleaned the reports repository to keep last 30 reports")
    else:
        logger.debug("Something messed up with the reports clean up")
        return("Unable to cleanup the Reports Folder")

def gitVerify(path,flag):
    '''Function gitVerify is verifying the given path against the flag that is being set'''
    repo = git.Repo(path)
    repo.remotes.origin.pull()
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit and flag:
        logger.info('The remote and local head are matching up hence the flag set is Valid')
        logger.info(current)
        logger.info(repo.head.commit)
    else:
        logger.error('The remote and local head are matching up hence the flag set is Valid')
        logger.error(current)
        logger.error(repo.head.commit)