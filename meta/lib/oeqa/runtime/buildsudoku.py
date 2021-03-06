from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import *
from oeqa.utils.targetbuild import TargetBuildProject

def setUpModule():
    if not oeRuntimeTest.hasFeature("tools-sdk"):
        skipModule("Image doesn't have tools-sdk in IMAGE_FEATURES")

class SudokuTest(oeRuntimeTest):

    @classmethod
    def setUpClass(self):
        self.restartTarget("-m 512")
        self.project = TargetBuildProject(oeRuntimeTest.tc.target,
                        "http://downloads.sourceforge.net/project/sudoku-savant/sudoku-savant/sudoku-savant-1.3/sudoku-savant-1.3.tar.bz2")
        self.project.download_archive()

    @skipUnlessPassed("test_ssh")
    def test_sudoku(self):
        self.assertEqual(self.project.run_configure(), 0,
                        msg="Running configure failed")

        self.assertEqual(self.project.run_make(), 0,
                        msg="Running make failed")

    @classmethod
    def tearDownClass(self):
        self.project.clean()
        self.restartTarget()
