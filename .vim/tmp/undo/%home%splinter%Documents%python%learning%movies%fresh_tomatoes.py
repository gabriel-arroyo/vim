Vim�UnDo� Y0�����pn���]F��_��ݿR��p �|^   �                 	   	   	   	       Y+�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Y+R    �                   �               5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             Y+�     �   �   �   �       �   �   �   �    5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Y+3     �   �   �   �              movie.__hash__5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Y+6     �   �   �                  movi_5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y+K    �         �       �         �    5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             Y+o    �                import media5�_�                 	           ����                                                                                                                                                                                                                                                                                                                                      �          V       Y+�     �   
             <meta charset="utf-8">�                <title>Fresh Tomatoes!</title>�                
    body {�                    padding-top: 80px;�                    }�                    #trailer .modal-dialog {�                    margin-top: 200px;�                    width: 640px;�                    height: 480px;�                    }�                    .hanging-close {�                    position: absolute;�                    top: -12px;�                     right: -12px;�      !              z-index: 9001;�       "              }�   !   #              #trailer-video {�   "   $              width: 100%;�   #   %              height: 100%;�   $   &              }�   %   '              .movie-tile {�   &   (              margin-bottom: 20px;�   '   )              padding-top: 20px;�   (   *              }�   )   +              .movie-tile:hover {�   *   ,              background-color: #EEE;�   +   -              cursor: pointer;�   ,   .              }�   -   /              .scale-media {�   .   0              padding-bottom: 56.25%;�   /   1              position: relative;�   0   2              }�   1   3              .scale-media iframe {�   2   4              border: none;�   3   5              height: 100%;�   4   6              position: absolute;�   5   7              width: 100%;�   6   8              left: 0;�   7   9              top: 0;�   8   :              background-color: white;�   9   ;              }�   <   >          /    // Pause the video when the modal is closed�   =   ?          Y    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {�   >   @          L    // Remove the src so the player itself gets removed, as this is the only�   ?   A          ;    // reliable way to ensure the video stops playing in IE�   @   B          *    $("#trailer-video-container").empty();�   A   C              });�   B   D          C    // Start playing the video whenever the trailer modal is opened�   C   E          =    $(document).on('click', '.movie-tile', function (event) {�   D   F          B    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')�   E   G          _    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';�   F   H          I    $("#trailer-video-container").empty().append($("<iframe></iframe>", {�   G   I              'id': 'trailer-video',�   H   J              'type': 'text-html',�   I   K              'src': sourceUrl,�   J   L              'frameborder': 0�   K   M              }));�   L   N              });�   M   O          0    // Animate in the movies when the page loads�   N   P          #    $(document).ready(function () {�   O   Q          F    $('.movie-tile').hide().first().show("fast", function showNext() {�   P   R          /    $(this).next("div").show("fast", showNext);�   Q   S              });�   R   T              });�   T   V              </head>�   U   W              '''�   Z   \          <body>�   [   ]          <!-- Trailer Video Modal -->�   \   ^           <div class="modal" id="trailer">�   ]   _          <div class="modal-dialog">�   ^   `          <div class="modal-content">�   _   a          J<a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">�   `   b          �<img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>�   a   c          </a>�   b   d          6<div class="scale-media" id="trailer-video-container">�   c   e          </div>�   d   f          </div>�   e   g          </div>�   f   h          </div>�   j   l          J    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">�   k   m              <div class="container">�   l   n              <div class="navbar-header">�   m   o          F    <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>�   n   p          
    </div>�   o   q          
    </div>�   p   r          
    </div>�   s   u              {movie_tiles}�   u   w              </body>�   v   x              </html>�   w   y              '''�   }             7<img src="{poster_image_url}" width="220" height="342">�   ~   �          <h2>{movie_title}</h2>�   �   �                  return content5�_�             	             ����                                                                                                                                                                                                                                                                                                                                                             Y+I    �         �          <link rel="stylesheet" "   R    "href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">5�_�                             ����                                                                                                                                                                                                                                                                                                                                      �          V       Y+Q    �   
             <meta charset="utf-8">�                <title>Fresh Tomatoes!</title>�                
    body {�                    padding-top: 80px;�                    }�                    #trailer .modal-dialog {�                    margin-top: 200px;�                    width: 640px;�                    height: 480px;�                    }�                    .hanging-close {�                    position: absolute;�                     top: -12px;�      !              right: -12px;�       "              z-index: 9001;�   !   #              }�   "   $              #trailer-video {�   #   %              width: 100%;�   $   &              height: 100%;�   %   '              }�   &   (              .movie-tile {�   '   )              margin-bottom: 20px;�   (   *              padding-top: 20px;�   )   +              }�   *   ,              .movie-tile:hover {�   +   -              background-color: #EEE;�   ,   .              cursor: pointer;�   -   /              }�   .   0              .scale-media {�   /   1              padding-bottom: 56.25%;�   0   2              position: relative;�   1   3              }�   2   4              .scale-media iframe {�   3   5              border: none;�   4   6              height: 100%;�   5   7              position: absolute;�   6   8              width: 100%;�   7   9              left: 0;�   8   :              top: 0;�   9   ;              background-color: white;�   :   <              }�   =   ?          /    // Pause the video when the modal is closed�   >   @          Y    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {�   ?   A          L    // Remove the src so the player itself gets removed, as this is the only�   @   B          ;    // reliable way to ensure the video stops playing in IE�   A   C          *    $("#trailer-video-container").empty();�   B   D              });�   C   E          C    // Start playing the video whenever the trailer modal is opened�   D   F          =    $(document).on('click', '.movie-tile', function (event) {�   E   G          B    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')�   F   H          _    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';�   G   I          I    $("#trailer-video-container").empty().append($("<iframe></iframe>", {�   H   J              'id': 'trailer-video',�   I   K              'type': 'text-html',�   J   L              'src': sourceUrl,�   K   M              'frameborder': 0�   L   N              }));�   M   O              });�   N   P          0    // Animate in the movies when the page loads�   O   Q          #    $(document).ready(function () {�   P   R          F    $('.movie-tile').hide().first().show("fast", function showNext() {�   Q   S          /    $(this).next("div").show("fast", showNext);�   R   T              });�   S   U              });�   U   W              </head>�   V   X              '''�   [   ]          <body>�   \   ^          <!-- Trailer Video Modal -->�   ]   _           <div class="modal" id="trailer">�   ^   `          <div class="modal-dialog">�   _   a          <div class="modal-content">�   `   b          J<a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">�   a   c          �<img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>�   b   d          </a>�   c   e          6<div class="scale-media" id="trailer-video-container">�   d   f          </div>�   e   g          </div>�   f   h          </div>�   g   i          </div>�   k   m          J    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">�   l   n              <div class="container">�   m   o              <div class="navbar-header">�   n   p          F    <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>�   o   q          
    </div>�   p   r          
    </div>�   q   s          
    </div>�   t   v              {movie_tiles}�   v   x              </body>�   w   y              </html>�   x   z              '''�   ~   �          7<img src="{poster_image_url}" width="220" height="342">�      �          <h2>{movie_title}</h2>�   �   �                  return content5��