*****************************************************
youtube-dl - download videos from popular-video sites
*****************************************************




Examples
========



Download a video
----------------


```
youtube-dl https://www.youtube.com/watch?v=fzSK2gAkdD8
```


Save video using YouTube video ID as filename
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```
youtube-dl --id https://www.youtube.com/watch?v=fzSK2gAkdD8
```


Download the video and subtitles
--------------------------------

```
youtube-dl --write-sub https://www.youtube.com/watch?v=fzSK2gAkdD8
```



Download just the subtitles
^^^^^^^^^^^^^^^^^^^^^^^^^^^


```
youtube-dl --skip-download --write-sub \
    https://www.youtube.com/watch?v=fzSK2gAkdD8
```


http://superuser.com/questions/927523/how-to-download-only-subtitles-of-videos-using-youtube-dl

