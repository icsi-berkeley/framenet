"""
@author: <seantrott@icsi.berkeley.edu>

Initializes FrameNetBuilder and FrameNet objects.
"""

from src.builder import *
import sys
from src.ecg_utilities import ECGUtilities as utils
#from src.valence_data import *

from src.hypothesize_constructions import *

from scripts import *

import csv



def main(data_path):
    frame_path = data_path + "frame/"
    relation_path = data_path + "frRelation.xml"
    lu_path = data_path + "lu/" 
    fnb = FramenetBuilder(frame_path, relation_path, lu_path)
    fn = fnb.read() #fnb.read()
    fn.build_relations()
    fn.build_typesystem()
    return fn, fnb




if __name__ == "__main__":
    fn, fnb = main(sys.argv[1])

    fnb.build_lus_for_frame("Motion", fn)




    
    
















    
    
    