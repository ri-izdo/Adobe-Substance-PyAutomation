from pysbs import context, sbsenum, sbsgenerator
from math import log

aContext = context.Context()
#aContext.getUrlAliasMgr().setAliasAbsPath(aAliasName = 'rlizardo', aAbsPath = "/Users/rlizardo/Desktop")

startPos = [48, 48, 0]
xOffset = [192, 0, 0]
yOffset = [0, 192, 0]

sbsDoc = sbsgenerator.createSBSDocument(aContext,
                        aFileAbsPath = "/Users/rlizardo/Desktop/Demo.sbs",
                        aGroupIdentifier = "RGB2PBR")

# Get graph 'SimpleMaterial'
aGraph = sbs.Doc.getSBSGraph(aGraphIdentifier = 'RGB2PBR')

#baseColor = aGraph.createComp

print(%s)