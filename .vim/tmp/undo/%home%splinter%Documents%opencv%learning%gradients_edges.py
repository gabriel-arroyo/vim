Vim�UnDo� ѫ1��8��T2^�ι�41d���e��)      &    edges = cv2.Canny(frame, 100, 200)            =       =   =   =    Y@o@    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Y?w     �                   5�_�                    	   .    ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �      
   	    5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �      	           5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �   	                  �   	            5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �               �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �                     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �                 cap.release()5�_�      	              
        ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �   	   
           5�_�      
           	   
        ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �   	             5�_�   	              
   
        ����                                                                                                                                                                                                                                                                                                                                                             Y?�     �   	   
           5�_�   
                 	        ����                                                                                                                                                                                                                                                                                                                                                             Y?�    �   	                �   	          5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             Y@l�     �      	          0    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@l�     �                   �      
       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@m     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@m     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@m     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@m     �   
              5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             Y@m     �   
                �   
          5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y@m/     �                   cv2.imshow('original')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y@m4     �                   �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y@m;     �                   cv2.imshow('laplacian')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@mG     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@mH     �                 5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             Y@mI     �   
                �   
          5�_�                       6    ����                                                                                                                                                                                                                                                                                                                                                             Y@md     �             �             5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             Y@mj     �               8    soblex = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             Y@mn     �               8    sobley = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)5�_�                       -    ����                                                                                                                                                                                                                                                                                                                                                             Y@mn     �               8    sobley = cv2.Sobel(frame, cv2.CV_64F, 0, 0, ksize=5)5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             Y@mt     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Y@mv     �               &    cv2.imshow('laplacian', laplacian)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Y@my     �               #    cv2.imshow('soblex', laplacian)5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             Y@m}     �               &    cv2.imshow('laplacian', laplacian)5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             Y@m�     �               #    cv2.imshow('soblex', laplacian)5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                             Y@m�     �                    cv2.imshow('soblex', soblex)5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                             Y@m�     �                    cv2.imshow('soblex', sobley)5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             Y@m�     �      
             �      
       5�_�   $   &           %   	       ����                                                                                                                                                                                                                                                                                                                                                             Y@n    �      
             frame = cv2.flip(frame,1)5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                               	                 V       Y@n<     �                �             5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                               	                 V       Y@n>     �                �             5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                               %                  v   %    Y@n�     �                     cv2.imshow('sobley', sobley)�                     cv2.imshow('soblex', soblex)�                &    cv2.imshow('laplacian', laplacian)5�_�   (   +           )           ����                                                                                                                                                                                                                                                                                                                                                  V        Y@n�    �                "#     cv2.imshow('sobley', sobley)�                "#     cv2.imshow('soblex', soblex)�                (#     cv2.imshow('laplacian', laplacian)5�_�   )   ,   *       +          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               ,    #     cv2.imshow('laplacian', laplacian)5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               +    #    cv2.imshow('laplacian', laplacian)5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               *    #   cv2.imshow('laplacian', laplacian)5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               &    #     cv2.imshow('soblex', soblex)5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               %    #    cv2.imshow('soblex', soblex)5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               $    #   cv2.imshow('soblex', soblex)5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               &    #     cv2.imshow('sobley', sobley)5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               %    #    cv2.imshow('sobley', sobley)5�_�   2   4           3          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               $    #   cv2.imshow('sobley', sobley)5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               )    #  cv2.imshow('laplacian', laplacian)5�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               #    #  cv2.imshow('soblex', soblex)5�_�   5   7           6          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               #    #  cv2.imshow('sobley', sobley)5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �                   �             5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �                   cv2.imshow('edges')5�_�   8   =           9          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               &    edges = cv2.Canny(frame, 100, 200)5�_�   9       :       =          ����                                                                                                                                                                                                                                                                                                                                                v       Y@o?    �               %    edges = cv2.Canny(frame, 50, 200)5�_�   9   ;       =   :      !    ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               $    edges = cv2.Canny(frame, 50, 50)5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               %    edges = cv2.Canny(frame, 100, 50)5�_�   ;               <      "    ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               &    edges = cv2.Canny(frame, 100, 100)5�_�   )           +   *          ����                                                                                                                                                                                                                                                                                                                                                v       Y@n�     �               +   #     cv2.imshow('laplacian', laplacian)5��