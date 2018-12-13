#!/usr/bin/env python3

print('''
//JS to show pop-up info about specific movie

//Vavigate to index
document.getElementById("banner").addEventListener('click', index_nav);

function index_nav() {
  var index = document.getElementById("index_nav");
  index.submit();
}

//Execute cgi (find) script
document.getElementById("find_it").addEventListener('click', submit_form);

function submit_form() {
  var form = document.getElementById("find_it_form");
  form.submit();
}

//Execute save script
document.getElementById("final_save").addEventListener('click', save_form);

function save_form() {
  if((document.getElementById("save_name").value) == ""){
    (document.getElementById("save_name").placeholder) = "ERROR: Must enter list name";
  } else {
    var save_form = document.getElementById("movie_list_submit");
    save_form.submit();
  }
}

//Add listeners
var api_key = "a09a65714522b9ac6c337dd5feb7a7a3";

result = document.getElementsByClassName("result");
for (var i = 0; i < result.length; i++) {
    result[i].addEventListener('dblclick', get_api_info);
    result[i].addEventListener('click', add_result);
}


function get_api_info() {

  var this_id = event.target.id;
  var requestURL = "https://api.themoviedb.org/3/movie/"+this_id+"?api_key="+api_key+"&language=en-US&append_to_response=credits"
  $.getJSON(requestURL, popUp);
}


function popUp(api_info) {
  console.log(api_info);

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


//Select list results ----------------------------------------------
function add_result() {
  var element = event.target;
  if(element.className == "result_sel") {
    element.className = "result";
  } else {
    element.className = "result_sel";
  }
}


//Move selected results to current list
document.getElementById("add_it").addEventListener('click', add_to_list);

function add_to_list() {
  var table = document.getElementById("results_table");
  var all_results = table.childNodes;

  var list_table = document.getElementById("list_table");

  for (var i=0; i < all_results.length; i++) {
    if (all_results[i].className == "result_sel") {
      all_results[i].className = "result";
      list_table.appendChild(all_results[i]);
    }
  }

  //all_results.forEach(function(entry) {
    //if (entry.className == "result_sel") {
      //entry.className = "result";
      //list_table.appendChild(entry);
    //}
  //});

}


//Controls
//Select All <<<ERROR (NOT CURRENTLY USED)
//document.getElementById("results_select_all").addEventListener('click', r_sel_all);
//function r_sel_all() {
  //var table = document.getElementById("results_table");
  //var all_results = table.childNodes;

  //all_results.forEach(function(entry) {
    //entry.className = "result_sel";
  //});

  //for (var i=0; i < all_results.length; i++) {
    //all_results[i].className = "result_sel";
  //}
//}

//Select None <<<ERROR (NOT CURRENTLY USED)
//document.getElementById("results_select_none").addEventListener('click', r_sel_none);
//function r_sel_none() {
  //var table = document.getElementById("results_table");
  //var all_results = table.childNodes;

  //for (var i=0; i < all_results.length; i++) {
    //all_results[i].className = "result";
  //}
//}

//UNDO
document.getElementById("list_undo").addEventListener('click', undo_result);
function undo_result() {
  var table = document.getElementById("results_table");
  var list_table = document.getElementById("list_table");
  var all_results = list_table.childNodes;

  for (var i=0; i < all_results.length; i++) {
    if (all_results[i].className == "result_sel") {
      all_results[i].className = "result";
      table.appendChild(all_results[i]);
    }
  }
}


//Save it --------------------------------------
document.getElementById("save_it").addEventListener('click', save_list);

function save_list() {
  var movies = [];
  var table = document.getElementById("list_table");
  var all_results = table.childNodes;

  for (var i=1; i < all_results.length; i++) {
    movies.push(all_results[i].textContent +" | "+ all_results[i].id);
  }
  var input = document.getElementById("save_input");
  input.value = movies;
  //alert(movies);



  //Pop-up for Saving -----------------------------------------------
  // Get the pop
  var modal = document.getElementById('savePop');

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
''')
