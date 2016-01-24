from src.builder import *
import sys
from src.ecg_utilities import ECGUtilities as utils
from src.valence_data import *

if __name__ == "__main__":
	data_path = sys.argv[1]
	frame_path = data_path + "frame/"
	relation_path = data_path + "frRelation.xml"
	lu_path = data_path + "lu/"	
	fnb = FramenetBuilder(frame_path, relation_path, lu_path)
	fn = fnb.read() #fnb.read()
	fn.build_relations()
	fn.build_typesystem()



	
	
	