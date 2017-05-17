

/*MENU NAV*/
/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

/*TOOL TIP

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
}
*/
/*TOOL TIP ATTEM #2 */
jQuery.noConflict();
(function($){
	$(document).ready(function(){
		$("[title]").style_my_tooltips({ 
			tip_follows_cursor:false, //boolean
			tip_delay_time:700, //milliseconds
			tip_fade_speed:300 //milliseconds
		});
		//dynamically added elements demo function
		$("a[rel='add new element']").click(function(e){
			e.preventDefault();
			$(this).attr("title","Add another element").parent().after("<p title='New paragraph title'>This is a new paragraph! Hover to see the title.</p>");
		});
	});
})(jQuery);

/*Bookmark in Browser*/
$(document).ready(function() {
  $("#bookmarkme").click(function() {
    if (window.sidebar) { // Mozilla Firefox Bookmark
      window.sidebar.addPanel(location.href,document.title,"");
    } else if(window.external) { // IE Favorite
      window.external.AddFavorite(location.href,document.title); }
    else if(window.opera && window.print) { // Opera Hotlist
      this.title=document.title;
      return true;
    }
  });
});

/*Bookmark in Chrome*/
javascript:(function(){var d=document,e=d.getElementById("#BookmarkChrome");e.value="some value";})();

/*POST LIST BOARD*/
