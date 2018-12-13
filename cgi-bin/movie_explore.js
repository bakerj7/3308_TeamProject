#!/usr/bin/env python3

print('''
//JS for explore page

window.addEventListener('load', pull_list_names);
function pull_list_names() {
  lists_table = document.getElementById("lists_table");
  for (var i = 0; i < localStorage.length; i++) {
      var key = localStorage.key(i);

      var newDiv = document.createElement('div');
      newDiv.textContent = key;
      newDiv.className = "list";
      lists_table.appendChild(newDiv);
      //var value = localStorage[key];
  }
  movie_list = document.getElementsByClassName("list");
  for (var i = 0; i < movie_list.length; i++) {
      movie_list[i].addEventListener('click', open_list);
  }
}


//Vavigate to index
document.getElementById("banner").addEventListener('click', index_nav);

function index_nav() {
  var index = document.getElementById("index_nav");
  index.submit();
}


//var requestURL = "https://api.themoviedb.org/3/genre/movie/list?api_key=a09a65714522b9ac6c337dd5feb7a7a3"
var api_key = "a09a65714522b9ac6c337dd5feb7a7a3";

movie_list = document.getElementsByClassName("list");
for (var i = 0; i < movie_list.length; i++) {
    movie_list[i].addEventListener('click', open_list(Null, Null));
}


//Open Movie list when clicked ----------------------------
function open_list(from, key_name) {

  var list_name;
  if (from == "search") {
    list_name = key_name;
  } else {
    list_name = event.target.textContent;
  }

  var list_title = document.getElementById('list_title');
  list_title.textContent = list_name;

  //Clear and populate movie items
  var list_table = document.getElementById('list_table');
  while (list_table.firstChild) {
    list_table.removeChild(list_table.firstChild);
  }
  var list_value = localStorage[list_name].split("<br>");
  for (var i = 0; i < list_value.length-1; i++) {
      movie_data = list_value[i].split(" | ");

      var newDiv = document.createElement('div');
      newDiv.textContent = movie_data[0];
      newDiv.className = "result";
      newDiv.id = movie_data[1];
      list_table.appendChild(newDiv);

  }



  result = document.getElementsByClassName("result");
  for (var i = 0; i < result.length; i++) {
      result[i].addEventListener('click', add_result);
      result[i].addEventListener('dblclick', get_api_info);
  }


  // Get the pop
  var modal = document.getElementById('myListPop');

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal
  modal.style.display = "block";

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
}


//Search list button ----------------------
find_it_btn = document.getElementById('find_it');
find_it_btn.addEventListener('click', search_for_list);

function search_for_list() {
  var list_name = document.getElementById('list_name_input');

  for (var i = 0; i < localStorage.length; i++) {
      var key = localStorage.key(i);

      if (key == list_name.value) {
        open_list("search", key);
        break;
      }
  }
  //Error messages
  if (list_name.value == "" ){
    list_name.placeholder = "ERROR: No Name Entered";
  } else {
    list_name.value = "";
    list_name.placeholder = "ERROR: List Not Found";
  }
}

//Get Lucky Search button ----------------------
find_it_btn = document.getElementById('get_lucky');
find_it_btn.addEventListener('click', lucky_list);

function lucky_list() {
    i = Math.floor(Math.random() * localStorage.length);
    var key = localStorage.key(i);
    open_list("search", key);
}



function get_api_info() {

  var this_id = event.target.id;
  var requestURL = "https://api.themoviedb.org/3/movie/"+this_id+"?api_key="+api_key+"&language=en-US&append_to_response=credits"
  $.getJSON(requestURL, popUp);
}


function popUp(api_info) {
  //console.log(api_info);

  //Update all movie info fields with api info ----------------------
  var poster = document.getElementById("poster_img");
  poster.src = "https://image.tmdb.org/t/p/w185" + api_info['poster_path'];

  var title = document.getElementById("title");
  title.textContent = api_info['title'];

  var title = document.getElementById("tagline");
  title.textContent = api_info['tagline'];

  var title = document.getElementById("overview");
  title.textContent = api_info['overview'];

  var title = document.getElementById("length");
  title.textContent = api_info['runtime'] + " mins";

  var title = document.getElementById("release");
  title.textContent = api_info['release_date'];

  //Genres
  var genres_txt = "";
  for (var i=0; i < (api_info['genres']).length; i++) {
    if(i != (api_info['genres']).length-1) {
      genres_txt += (api_info['genres'][i])['name'] + ", ";
    } else {
      genres_txt += (api_info['genres'][i])['name'];
    }
  }

  var title = document.getElementById("genre");
  title.textContent = genres_txt;

  //Actors (first 10 or less)
  var actor_txt = "";
  num_actors = Math.min((api_info['credits']['cast']).length, 10);
  for (var i=0; i < num_actors; i++) {
    actor_txt += (api_info['credits']['cast'][i])['name'] + " (" + (api_info['credits']['cast'][i])['character'] +"), ";
  }

  var title = document.getElementById("actors");
  title.textContent = actor_txt;


  var title = document.getElementById("rating");
  title.textContent = api_info['vote_average'];

  var title = document.getElementById("website");
  title.textContent = api_info['homepage'];
  title.href = api_info['homepage'];


  //Pop-up functions -----------------------------------------------
  // Get the pop
  var modal = document.getElementById('myPop');

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[1];

  // When the user clicks the button, open the modal
  modal.style.display = "block";

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
}


//Select list results ----------------------------------------------
function add_result() {
  var element = event.target;
  if(element.className == "result_sel") {
    element.className = "result";
  } else {
    element.className = "result_sel";
  }
}

''')
