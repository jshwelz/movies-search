from flask import Blueprint, jsonify
from flask import request
from service.movies import get_titles_by_keyword, get_tags_by_keyword, get_all_movies, get_genres_by_keyword
movies = Blueprint('movies', __name__)


@movies.route('/', methods=['GET'])
def get_movies():
	"""Movies list view.
	---
	get:
		summary: 'List all Movies'
		description: 'Returns all the movies'
		operationId: 'ListMovies'
		responses:
			401:
				description: 'UnAuthorized'
			500:
				description: 'Server error'
			'200':
				content:
					application/json:
						schema: 'Movie'
				description: 'Movies List'
				schema:
					$ref: '#/components/schemas/Movie'
	"""

	limit_per_page = request.args.get('limit', default=1, type=int)
	page_number = request.args.get('page', default=1, type=int)
	keyword = request.args.get('key', default=None, type=str)
	filter = request.args.getlist('filter')
	request_options = {'page_number': page_number, 'limit_per_page': limit_per_page, 'filter': filter}
	res = {}
	if keyword:
		data = []
		search = "%{}%".format(keyword)
		data.append({'titles': get_titles_by_keyword(search, request_options)})
		data.append({'genres': get_genres_by_keyword(search, request_options)})
		data.append({'tags': get_tags_by_keyword(search, request_options)})
		total_rows = data[0]['titles']['total'] + data[1]['genres']['total'] + data[2]['tags']['total']
		res.update({'result_type': 'general', 'data': data, 'count': limit_per_page, 'total': total_rows,
		            'page': request_options['page_number'], 'pageCount': (total_rows // limit_per_page)})

	else:
		return jsonify(get_all_movies(request_options)), 200

	return jsonify(res), 200
