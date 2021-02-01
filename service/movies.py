from globals import db
from models.Movies import MoviesModel
from models.Tags import TagsModel
from models.Ratings import RatingsModel
from schemas.movies import movie_schema
from schemas.result import result_schema


def get_titles_by_keyword(keyword, request_options):
	q = db.session.query(MoviesModel.movieId, MoviesModel.title, MoviesModel.genres, RatingsModel.rating,
	                     RatingsModel.userId, TagsModel.tag) \
		.join(RatingsModel, MoviesModel.movieId == RatingsModel.movieId, isouter=True) \
		.join(TagsModel, MoviesModel.movieId == TagsModel.movieId, isouter=True).filter(MoviesModel.title.like(keyword))
	q = q.group_by(MoviesModel.title)
	return get_schema(q, request_options)


def get_genres_by_keyword(keyword, request_options):
	q = db.session.query(MoviesModel.movieId, MoviesModel.title, MoviesModel.genres, RatingsModel.rating,
	                     RatingsModel.userId, TagsModel.tag) \
		.join(RatingsModel, MoviesModel.movieId == RatingsModel.movieId, isouter=True) \
		.join(TagsModel, MoviesModel.movieId == TagsModel.movieId, isouter=True).filter(MoviesModel.genres.like(keyword))
	return get_schema(q, request_options)


def get_tags_by_keyword(keyword, request_options):
	q = db.session.query(MoviesModel.movieId, MoviesModel.title, MoviesModel.genres, RatingsModel.rating,
	                     RatingsModel.userId, TagsModel.tag) \
		.join(RatingsModel, MoviesModel.movieId == RatingsModel.movieId, isouter=True) \
		.join(TagsModel, MoviesModel.movieId == TagsModel.movieId, isouter=True).filter(TagsModel.tag.like(keyword))
	q = q.group_by(MoviesModel.title)
	return get_schema(q, request_options)


def get_all_movies(request_options):
	q = db.session.query(MoviesModel.movieId, MoviesModel.title, MoviesModel.genres, RatingsModel.rating,
	                     RatingsModel.userId, TagsModel.tag) \
		.join(RatingsModel, MoviesModel.movieId == RatingsModel.movieId, isouter=True) \
		.join(TagsModel, MoviesModel.movieId == TagsModel.movieId, isouter=True)
	if request_options['filter']:
		filters_list = list(request_options['filter'])
		filters = {n.split(',')[0]: n.split(',')[1] for n in filters_list}

		for attr, value in filters.items():
			if attr == 'userId':
				q = q.filter(getattr(RatingsModel, attr) == int(value))
			if attr == 'movieId':
				q = q.filter(getattr(MoviesModel, attr) == int(value))
			if attr == 'title':
				q = q.filter(getattr(MoviesModel, attr).like("%{}%".format(value)))
			if attr == 'tag':
				q = q.filter(getattr(TagsModel, attr).like("%{}%".format(value)))
	return get_schema(q, request_options)


def get_schema(query, request_options):
	q = query.group_by(MoviesModel.title)
	titles_list = q.paginate(request_options['page_number'], request_options['limit_per_page'], error_out=False)
	total_per_page = titles_list.per_page
	total_rows = titles_list.total
	record_items = titles_list.items
	movies_list = movie_schema.dump(record_items, many=True)
	res = {}
	res.update({'result_type': 'general', 'data': movies_list, 'count': total_per_page, 'total': total_rows,
	            'page': request_options['page_number'], 'pageCount': (total_rows // total_per_page)})
	return result_schema.dump(res)
