serve:
	docker run -it --rm -p 8888:8888 \
	       --volume ./:/code \
	       --workdir /code \
	       jupyter/pyspark-notebook
