# Gallery对象

## 获取Gallery对象

| 方法                   | 说明            |
|----------------------|---------------|
| Project.GetGallery() | 返回 Gallery 对象 |

```python
import DaVinciResolveScript as dvr_script

resolve = dvr_script.scriptapp("Resolve")

# 获取 ProjectManager 对象
project_manager = resolve.GetProjectManager()

# 获取当前项目返回 project 对象
project = project_manager.GetCurrentProject()

# 获取Gallery对象
gallery = project.GetGallery()

```

## Gallery.GetCurrentStillAlbum()

- 返回 galleryStillAlbum 对象

将当前album作为GalleryStillAlbum对象返回。

```python
# return galleryStillAlbum object
gallery_still_album = gallery.GetCurrentStillAlbum()
```

## Gallery.GetGalleryStillAlbums()

- 返回 [galleryStillAlbum]

以GalleryStillAlbum对象列表的形式返回gallery albums对象。

```python
# return [galleryStillAlbum]
gallery_still_albums = gallery.GetGalleryStillAlbums()
```

## Gallery.SetCurrentStillAlbum(galleryStillAlbum)

- 返回 Bool

将当前album设置为指定的GalleryStillAlbum对象的“galleryStillAlbum”。

```python
# return Bool
res = gallery.SetCurrentStillAlbum(galleryStillAlbum)
```

## Gallery.GetAlbumName(galleryStillAlbum)

- 返回 string

返回GalleryStillAlbum对象“GalleryStillAlbum”的名称。

```python
# return string
gallery_still_album = gallery.GetCurrentStillAlbum()
album_name = gallery.GetAlbumName(gallery_still_album)
```

## Gallery.SetAlbumName(galleryStillAlbum, albumName)

- 返回 Bool

将GalleryStillAlbum对象的名称“GalleryStillAlbum”设置为“albumName”

```python
# return Bool
gallery_still_album = gallery.GetCurrentStillAlbum()
res = gallery.SetAlbumName(gallery_still_album, "test_album_name")
```