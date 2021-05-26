from flask import Flask, render_template, request
import sys, ast, os, json
import plotly
import plotly.graph_objects as go
import ast

app = Flask(__name__)

tweets = {'users': ['RchavezRuben'], 'text': ['RT @KenDilanianNBC: Imagine if, two months ago, a competent federal government had led a World War II-level effort to ramp up production of…'], 'id': [123456789]}
tweet_counters = {'positive': 23, 'neutral': 23, 'negative': 4, 'total': 50}
word_counts = {'words': ['COVID19', 'Quarantine'], 'counts': [16, 50]}
most_used_hashtags = {'labels': [], 'negative': [], 'neutral': [], 'positive': []}
most_active_users = {'labels': [], 'negative': [], 'neutral': [], 'positive': []}
most_mentioned_users = {'labels': [], 'negative': [], 'neutral': [], 'positive': []}
jqCloud_word_count = []


@app.route("/")
def home_page():
    global tweets
    global tweet_counters
    global most_used_hashtags
    global word_counts
    global most_active_users
    global most_mentioned_users
    global jqCloud_word_count

    print("Tweets variable", file=sys.stderr)
    print(tweets, file=sys.stderr)
    print("word count variable", file=sys.stderr)
    print(word_counts, file=sys.stderr)
    print("hashtag variable", file=sys.stderr)
    print(most_used_hashtag, file=sys.stderr)
    print(word_counts['words'], file=sys.stderr)
    
    wc = dict(zip(word_counts['words'], word_counts['counts']))
    jqCloud_word_count = [{'text': word, 'weight': count} for word, count in wc.items()]

    return render_template(
            'index.html',
            tweet_counters=tweet_counters,
            tweets=zip(tweets['users'], tweets['text'], tweets['id']),
            wordcounts=word_counts,
            most_used_hashtags=most_used_hashtags,
            most_active_users=most_active_users,
            most_mentioned_users=most_mentioned_users)

@app.route('/update_sentiments', methods=['POST'])
def update_sentiments():
    global tweet_counters

    print(request.form)

    tweet_counters['positive'] = ast.literal_eval(request.form['positive'])
    tweet_counters['neutral'] = ast.literal_eval(request.form['neutral'])
    tweet_counters['negative'] = ast.literal_eval(request.form['negative'])
    tweet_counters['total'] = ast.literal_eval(request.form['total'])

    return "success", 200

@app.route('/update_tweets', methods=['POST'])
def update_tweet_data():
    global tweets
    
    print(request.form)
    
    tweets['users'] = ast.literal_eval(request.form['user'])
    tweets['text'] = ast.literal_eval(request.form['text'])
    tweets['id'] = ast.literal_eval(request.form['id'])
    tweets['id'] = [str(tweet_id) for tweet_id in tweets['id']]
    
    return "success", 200


@app.route('/update_counts', methods=['POST'])
def update_counts():
    global word_counts
    
    print(request.form)
    
    word_counts['words'] = ast.literal_eval(request.form['words'])
    word_counts['counts'] = ast.literal_eval(request.form['counts'])
    print("Updated word counts - ",  word_counts)
    return "success", 200


@app.route('/update_hashtagcounts', methods=['POST'])
def update_hashtagcounts():
    global most_used_hashtags
    
    print(request.form)
    
    most_used_hashtags['labels'] = ast.literal_eval(request.form['labels'])
    most_used_hashtags['negative'] = ast.literal_eval(request.form['negative'])
    most_used_hashtags['neutral'] = ast.literal_eval(request.form['neutral'])
    most_used_hashtags['positive'] = ast.literal_eval(request.form['positive'])

    print("Updated hashtag counts - ",  most_used_hashtags)
    return "success", 200


@app.route('/update_most_active_users', methods=['POST'])
def update_most_active_users_data():
    global most_active_users
    if not request.form not in request.form:
        return "error", 400

    most_active_users['labels'] = ast.literal_eval(request.form['label'])
    most_active_users['negative'] = ast.literal_eval(request.form['negative'])
    most_active_users['neutral'] = ast.literal_eval(request.form['neutral'])
    most_active_users['positive'] = ast.literal_eval(request.form['positive'])

    return "success", 200

@app.route('/update_most_mentioned_users', methods=['POST'])
def update_most_mentioned_users_data():
    global most_mentioned_users
    if not request.form not in request.form:
        return "error", 400
    
    most_mentioned_users['labels'] = ast.literal_eval(request.form['label'])
    most_mentioned_users['negative'] = ast.literal_eval(request.form['negative'])
    most_mentioned_users['neutral'] = ast.literal_eval(request.form['neutral'])
    most_mentioned_users['positive'] = ast.literal_eval(request.form['positive'])
    
    return "success", 201


@app.route('/sentiments', methods=['GET'])
def refresh_sentiments():
    global tweet_counters
    print(tweet_counters)
    return tweet_counters


@app.route('/tweets', methods=['GET'])
def tweets_refresh():
    global tweets
    output = json.dumps(tweets)
    print(output)
    return output

@app.route('/word_cloud', methods=['GET'])
def word_cloud():
    global jqCloud_word_count
    global word_counts
    wc = dict(zip(word_counts['words'], word_counts['counts']))
    jqCloud_word_count = [{'text': word, 'weight': count} for word, count in wc.items()]
    output = json.dumps(jqCloud_word_count)
    print(output)
    return output


@app.route('/word_counts', methods=['GET'])
def refresh_counts():
    global most_used_hashtag
    output = json.dumps(word_counts)
    print(output)
    return output


@app.route('/refresh_most_active_users')
def refresh_most_active_users_data():
    global most_active_users

    output = json.dumps(most_active_users)
    print(output)
    return output


@app.route('/refresh_most_mentioned_users')
def refresh_most_mentioned_users_data():
    global most_mentioned_users

    output = json.dumps(most_mentioned_users)
    print(output)
    return output


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run(debug = True)
