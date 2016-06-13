var url = "https://gist.githubusercontent.com/d3byex/e5ce6526ba2208014379/raw/8fefb14cc18f0440dc00248f23cbf6aec80dcc13/walking_dead_s5.csv";
d3.csv(url,function(error,data){
  var mappedAndConverted = data.map(function(d){
    return {
      Episode: +d.Episode,
      USViewers: +d.USViewers,
      Title: d.Title
    }
  });
  console.log(mappedAndConverted);
});
