var url = "https://gist.githubusercontent.com/d3byex/e5ce6526ba2208014379/raw/8fefb14cc18f0440dc00248f23cbf6aec80dcc13/walking_dead_s5.json";
d3.json(url,function(error,data){
  console.log(data[0]);
});
console.log("Data in D3.js is loaded asynchronously");
