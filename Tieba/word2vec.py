import gensim
model = gensim.models.Word2Vec.load('/Users/shahaoran/Downloads/word2vec/word2vec/word2vec_wx')
print(model.most_similar(u'就业'))
# a = \
# 0.25 * 4.3 + \
# 2.0	* 4 + \
# 2.0	* 2.7 + \
# 2.0	* 3.3 + \
# 3.0	* 3 + \
# 2.0	* 3 + \
# 2.0	* 3.7 + \
# 2.0	* 3 + \
# 2.5	* 3.3 + \
# 3.5	* 3 + \
# 2.5	* 3.7 + \
# 2.0	* 3.3 + \
# 0.25 * 3.7 + \
# 2.5	* 2 + \
# 3.0	* 3.7 + \
# 2.0	* 3.7 + \
# 1.0	* 3.9 + \
# 2.0	* 3.7 + \
# 2.5	* 4.3 + \
# 3.0	* 4 + \
# 4.5	* 2.3 + \
# 3.5	* 3.3 + \
# 3.5	* 3.3 + \
# 0.75 * 2.7 + \
# 2.5	* 2 + \
# 3.0	* 3.3 + \
# 0.25 * 2.3 + \
# 3.0	* 2.7 + \
# 3.0	* 2.3 + \
# 2.5	* 3 + \
# 1.0	* 3 + \
# 2.0	* 3 + \
# 1.0	* 3.9 + \
# 5.0	* 3.3 + \
# 5.0	* 1 + \
# 3.0	* 2 + \
# 2.5	* 4 + \
# 0.75 * 2.3 + \
# 3.0	* 2.3 + \
# 0.25 * 3.3 + \
# 2.5	* 3.7 + \
# 6.0	* 2.3 + \
# 3.0	* 3 + \
# 1.0	* 3 + \
# 4.0	* 2.3 + \
# 2.0	* 1.3 + \
# 1.0	* 4 + \
# 2.0	* 4 + \
# 0.75 * 3 + \
# 1.0	* 3.7 + \
# 3.0	* 4 + \
# 0.25 * 3 + \
# 6.0	* 1 + \
# 2.5	* 3.7 + \
# 1.0 * 3 + \
# 4.0	* 3 + \
# 4.0	* 3.7 + \
# 0.75 * 4 + \
# 1.5	* 2.3 + \
# 1.5	* 3.7 + \
# 2.0	* 3.3
#
# b = \
# 0.25 + \
# 2.0 + \
# 2.0 + \
# 2.0 + \
# 3.0 + \
# 2.0 + \
# 2.0 + \
# 2.0 + \
# 2.5 + \
# 3.5 + \
# 2.5 + \
# 2.0 + \
# 0.25 + \
# 2.5 + \
# 3.0 + \
# 2.0 + \
# 1.0 + \
# 2.0 + \
# 2.5 + \
# 3.0 + \
# 4.5 + \
# 3.5 + \
# 3.5 + \
# 0.75 + \
# 2.5 + \
# 3.0 + \
# 0.25 + \
# 3.0 + \
# 3.0 + \
# 2.5 + \
# 1.0 + \
# 2.0 + \
# 1.0 + \
# 5.0 + \
# 3.0 + \
# 2.5 + \
# 0.75 + \
# 3.0 + \
# 0.25 + \
# 2.5 + \
# 6.0 + \
# 3.0 + \
# 1.0 + \
# 4.0 + \
# 2.0 + \
# 1.0 + \
# 2.0 + \
# 0.75 + \
# 1.0	+ \
# 3.0 + \
# 0.25 + \
# 6.0 + \
# 2.5 + \
# 1.0 + \
# 4.0 + \
# 4.0 + \
# 0.75 + \
# 1.5 + \
# 1.5 + \
# 2.0
# print(a)
# print(b)
# print(a/b)