# coding=UTF-8
import os
import sys
import commands

binaryName = "yourapp"
bundleName = "yourapp.app"
bundleFrameworkDir = "Contents/Frameworks/"
bundleBinaryDir = "Contents/MacOS/"
bundleLibraryList = [];
systemFrameworkDir = "/Library/Frameworks/"
keyWordList = ["Qt"]

# 这里我给出一个我写的打包的Python脚本半成品,思想跟手动敲命令是一样的，
# 只不过用脚本实现自动化了同时递归检查并将缺少的库考到bundle目录中。
# 脚本中针对QT的库进行打包了，如果希望把其他的依赖库也打包的话在keywordList里边添加相应的关键字就好了

# add more keywords to work better

def hasKeyWord(word):
    for it in keyWordList:
        if word.find(it) != -1:
            return True
    return False


def findApp(name):
    return name + bundleBinaryDir + binaryName


def getBundleDependsInfo(app):
    dependList = commands.getoutput("otool -L " + app).replace("\t", "").split("\n");
    del (dependList[0])
    dependList = [item.split(" ")[0] for item in dependList if hasKeyWord(item)];
    return dependList


def copyLibrary(base, src, dst):
    systemFullPath = src
    print "library %s depend %s" % (os.path.basename(base), os.path.basename(dst))
    if not os.path.exists(dst):
        bundleFullPath = os.path.dirname(dst)
        os.system("mkdir -p %s" % (bundleFullPath))
        os.system("cp %s %s" % (systemFullPath, bundleFullPath))
        infoList = getBundleDependsInfo(dst)
        copyDependFiles(dst, infoList)
        os.system("install_name_tool -id @executable_path/../Frameworks/%s %s" % (src, dst))
    os.system("install_name_tool -change %s @executable_path/../Frameworks/%s %s" % (src, src, base))


def getFrameworkName(dirname):
    if dirname.find("framework") == -1:
        return
    while not dirname.endswith("framework"):
        dirname = os.path.dirname(dirname)
    return dirname


def copyFrameworkExtDir(src):
    sysPath = systemFrameworkDir + src
    destPath = ""
    if not os.path.exists(sysPath):
        return
    frameworkPath = getFrameworkName(sysPath)
    frameWorkName = getFrameworkName(src)
    bundlePath = bundleName + "/" + bundleFrameworkDir + frameWorkName + "/"
    for it in bundleFrameworkExtDir:
        destPath = bundlePath + it
        srcPath = frameworkPath + "/" + it
        if not os.path.exists(destPath) and os.path.exists(srcPath):
            print "copying %s %s" % (frameWorkName, it)
            os.system("cp -r %s %s" % (srcPath, destPath))


def copyFramework(base, src, dst):
    print "framework %s depend %s" % (os.path.basename(base), os.path.basename(dst))
    systemFullPath = systemFrameworkDir + src
    if not os.path.exists(dst):
        bundleFullPath = os.path.dirname(dst)
        os.system("mkdir -p %s" % (bundleFullPath))
        os.system("cp %s %s" % (systemFullPath, bundleFullPath))
        copyFrameworkExtDir(src)
        infoList = getBundleDependsInfo(dst)
        copyDependFiles(dst, infoList)
        ("install_name_tool -id @executable_path/../Frameworks/%s %s" % (src, dst))
        os.system("install_name_tool -id @executable_path/../Frameworks/%s %s" % (src, dst))
    os.system("install_name_tool -change %s @executable_path/../Frameworks/%s %s" % (src, src, base))


def copyDependFiles(base, infoList):
    targetDir = ""
    for it in infoList:
        targetDir = bundleName + "/" + bundleFrameworkDir + it
        if it.find("framework") != -1:
            copyFramework(base, it, targetDir)
        else:
            copyLibrary(base, it, targetDir)


def makeBundleDirs():
    os.system("mkdir -p " + bundleName + "/" + bundleFrameworkDir)


if __name__ == "__main__":
    target = findApp(bundleName + "/")
    makeBundleDirs()
    infoList = getBundleDependsInfo(target)
    copyDependFiles(target, infoList)
