$(document).ready(function () {
   $.ajax({url: '/word_cloud', success: function (data) {
       var words_data = $.parseJSON(data);
       $('#div1').jQCloud(words_data, {
           autoResize: true
       });
   }});
});


setInterval(function(){
    $.ajax({url: '/word_cloud', success: function(data) {
    var words_data = $.parseJSON(data);
    $('#first').html("")
    $('#first').jQCloud(words_data, {
               autoResize: true
       });
    }});
},5000);


setInterval(function(){
    $.ajax({url: '/tweets', success: function(data) {
    var tweets_data = $.parseJSON(data);
    console.log(tweets_data);
    var tweets_text = tweets_data['text'];
    $('#RawTweets').html("")
    $("#RawTweets").append("<h3><center>Most Relevant Tweets</center></h3>")
    $.each(tweets_text, function(i, item) {
	    var link = "https://twitter.com/" + tweets_data['users'][i] + "/status/" + tweets_data['id'][i];
            $("#RawTweets").append("<div class=\"card\">" + "<a href=" + link + ">" + item + "</a></div>");
    });
    }});
},5000);




