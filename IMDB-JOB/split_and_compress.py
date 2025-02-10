from filesplit.split import Split

split = Split(inputfile="imdb.zip", outputdir="zip/")
split.bysize(size=94371840)
