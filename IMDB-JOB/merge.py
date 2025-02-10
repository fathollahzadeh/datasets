from filesplit.split import Split
from filesplit.merge import Merge
from os.path import dirname
import os

module_path = dirname(__file__)
merge = Merge(inputdir=fname_zip, outputdir=module_path, outputfilename="imdb.zip")
merge.merge()
