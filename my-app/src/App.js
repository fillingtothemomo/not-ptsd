import "./App.css";
import React, { useEffect, lazy } from "react";
import router from ""
import list from "../../api/media/manga_covers/default-avatar-profile-icon-of-social-media-user-vector_D4eX6c4.jpg";
// const importtt = lazy(() =>
//   import(
//     "../../api/media/manga_covers/default-avatar-profile-icon-of-social-media-user-vector_D4eX6c4.jpg"
//   )
// );
function App() {
  // importtt();
  const coverImage = "xyz,abc,erjk,wd,jnlw"
  const coverImageArray = coverImage.split(",");
  console.log(coverImageArray);
  let hi = 5;
  console.log(hi);
  return (
    <main>
      <h1>Manga Maestro</h1>
      {coverImageArray.map((coverImage) => {
        return <img src={coverImage} ></img>
      })}
    </main>
  );
}

export default App;
