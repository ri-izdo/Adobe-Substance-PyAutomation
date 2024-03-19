# Import sbs
from __future__ import unicode_literals
import logging
log = logging.getLogger(__name__)
import os
import sys

try:
    import pysbs
except ImportError:
    try:
        pysbsPath = bytes(__file__).decode(sys.getfilesystemencoding())
    except:
        pysbsPath = bytes(__file__,
            sys.getfilesystemencoding()).decode(sys.getfilesystemencoding())
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(pysbsPath[0], '..'))))

from pysbs import python_helpers
from pysbs import sbsgenerator
from pysbs import sbsenum
from pysbs import context
from pysbs.api_decorators import doc_source_code


@doc_source_code

def function(aDestFileAbsPath):
    """
    Create a subsatance with a very simple material definition: uniform colors for
        BaseColor, Roughness and Metallic, and
    save it to '~Desktop/demo.sbs'

    :param aDestFileAbsPath: The absolute path of the result SBS file
    :type aDestinationFileAbsPath: str
    :return: Nothing
    """
    aContext = context.Context()
    aContext.getUrlAliasMgr().setAliasAbsPath(aAliasName = 'demo', aAbsPath = aDestFileAbsPath)

    startPos = [48, 48, 0]
    xOffset = [192, 0, 0]
    yOffset = [0, 192, 0]

    try:
        # Create a new SBSDocument grom scratch, with a graph named 'SimpleMaterial'
        sbsDoc = sbsgenerator.createSBSDocument(aContext,
                                                aFileAbsPath = aDestFileAbsPath,
                                                aGraphIdentifier = 'SimpleMaterial')
        # Get the graph 'SimpleMaterial"
        aGraph = sbsDoc.getSBSGraph(aGraphIdentifier = 'SimpleMaterial')

        # Create BaseColor input node
        baseColor = aGraph.createCompFilterNode(aFilter = sbsenum.FilterEnum.UNIFORM,
                            aParameters = {sbsenum.CompNodeParamEnum.OUTPUT_COLOR: [ 1,
                            0, 1, 1]},
                            aGUIPos = startPos)

        # Create Basecolor output node
        # Create three Output nodes, for BaseColor, Roughness and Metallic
        outBaseColor = aGraph.createOutputNode(aIdentifier = 'BaseColor',
                            aGUIPos = baseColor.getOffsetPosition(xOffset),
                            aUsages = {sbsenum.UsageEnum.BASECOLOR: {
                                sbsenum.UsageDataEnum.COMPONENTS:sbsenum.ComponentsEnum.RGBA}})


        # Connect nodes

        aGraph.connectNodes(aLeftNode = baseColor, aRightNode = outBaseColor)

        # Write back the document structure into the destination .sbs file.
        sbsDoc.writeDoc()
        log.info("=> Resulting substance saved at %s", aDestFileAbsPath)

    except BaseException as error:
        log.error("!!! [demo] Failed to create the new package")
        raise error


if __name__ == "__main__":
    aDestFileAbsPath = "/Users/rlizardo/Desktop/demo.sbs"
    function(aDestFileAbsPath)