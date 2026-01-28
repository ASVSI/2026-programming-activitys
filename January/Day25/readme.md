# temperally_remove_images_from the chrome.md
### before that `allow pasting` as chrome will not allow to paste code directly into the console
- right click
- inspect
- console
- paste the below code
```js
const style = document.createElement('style');
style.innerHTML = 'img { display: none !important; }';
document.head.appendChild(style);
```
