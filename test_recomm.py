import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_base = pd.read_csv('main/data/ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('main/data/ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')
print ratings_base.shape, ratings_test.shape

import graphlab

train_data = graphlab.SFrame(ratings_base)
test_data = graphlab.SFrame(ratings_test)

#Train Model
popularity_model = graphlab.popularity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating')

item_sim_model_pearson = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating', similarity_type='pearson')


item_sim_model_jaccard = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating', similarity_type='jaccard')

item_sim_model_cosine = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id', target='rating', similarity_type='cosine')
#Make Recommendations:
#item_sim_recomm = item_sim_model.recommend(users=range(1,6),k=5)
#item_sim_recomm.print_rows(num_rows=25)

model_performance = graphlab.compare(
    test_data,
    [
        popularity_model,
        item_sim_model_pearson,
        item_sim_model_jaccard,
        item_sim_model_cosine,
    ]
)
graphlab.show_comparison(
    model_performance,
    [
        popularity_model,
        item_sim_model_pearson,
        item_sim_model_jaccard,
        item_sim_model_cosine,
    ]
)

import pdb
pdb.set_trace()
