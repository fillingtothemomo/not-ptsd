"use client"
import React from 'react'
function AddManga() {
    const [mangaTitle, setMangaTitle] = React.useState("");
    const [mangaAuthor, setMangaAuthor] = React.useState("");
    const [mangaDiscription, setMangaDiscription] = React.useState("");
    // const [mangaCoverImage, setMangaCoverImage] = React.useState();
    const handleClick = () => {
        console.log("clicked");
        console.log(mangaTitle,mangaAuthor,mangaDiscription,);
        
        
    }
  return (
   <main>
    <form>
    Manga Title: <input type="text" placeholder="Manga Title" onChange={e=>setMangaTitle(e.target.value)}></input><br/>
    Manga Author: <input type="text" placeholder="Manga Author" onChange={e=>setMangaAuthor(e.target.value)}></input><br/>
    Manga Discription: <textarea placeholder="Manga Discription" onChange={e=>setMangaDiscription(e.target.value)}></textarea><br/>
    {/* Manga Cover Image: <input type="file" accept="image/*" onChange={e=>setMangaCoverImage(e.target.files[0])}></input><br/> */}
    <button type='submit' onClick={handleClick}>Add Manga</button></form>
   </main>
  )
}

export default AddManga