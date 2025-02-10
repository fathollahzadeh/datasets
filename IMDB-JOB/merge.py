from filesplit.split import Split
from filesplit.merge import Merge
import os


fname_zip = "zip/"
merge = Merge(inputdir=fname_zip, outputdir="zip/", outputfilename="imdb.zip")
merge.merge()
