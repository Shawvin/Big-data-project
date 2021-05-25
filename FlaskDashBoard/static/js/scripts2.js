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


setInterval(function(){
    $.ajax({url: '/word_counts', success: function(data) {
        var counts_data = $.parseJSON(data);
        var data = [{
		x: counts_data['words'],
		y: counts_data['counts'],
		type: 'bar',
		text: counts_data['counts'].map(String),
		textposition: 'auto',
		hoverinfo: 'none',
		marker: {
			color: 'rgb(220, 248, 198)',
			opacity: 0.6,
			line: {
				color: 'rgb(8, 48, 107)',
				width: 1.5
			}
		}
        }];

        var layout = {
		title: 'Most used terms',
		barmode: 'stack'
        };

        Plotly.newPlot('second', data, layout);
    }});
},5000);


setInterval(function(){
    $.ajax({url: '/graph', success: function(data) {
        var graphs = $.parseJSON(data);
        var layout = {
		title: 'Real time tweets geo location!',
		font: {size: 10},
		showlegend: false,
        };

        var config = {responsive: true};
        Plotly.newPlot('third', graphs, layout, config);
    }});
}, 5000);


setInterval(function(){
    $.ajax({
	url: '/sentiments',
	success: function(data) {
		$("#total_counter_value").html(data['total'])
		$("#positive_counter").html(data['positive'] + " %")
		$("#neutral_counter").html(data['neutral'] + " %")
		$("#negative_counter").html(data['negative'] + " %")
	}
    });
},5000);
