"use client";
import React, { useEffect } from 'react'
import axios  from "axios"
import { useRouter } from 'next/navigation'
import { useSearchParams } from 'next/navigation'
import "../../styles/manga.css";
function Manga() {
  const searchParams = useSearchParams()
  const router = useRouter()
  const [chapterPages, setChapterPages] = React.useState("");
  const mangaId  = searchParams.get("id");
  var chapter = parseInt(searchParams.get("chap")!)||1;
  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/mangas/get_base64/"+mangaId+"_"+chapter).then((res)=>{setChapterPages(res.data["base64_images"])
  // console.log(res.data["base64_images"]);
  })
  },[chapter])
  const chapterPagesbase64 = chapterPages.split(",")
  console.log(chapterPagesbase64);
  
  return (
    <div>
      <center>
        Manga Name: {mangaId} <br/>
        Chapter No: {chapter}<br />
        <button className='prev_button p-2' onClick={()=>router.push(`/manga?id=${mangaId}&chap=${--chapter}`)}>Previous Chapter</button>&nbsp;<button className='next_button p-2' onClick={()=>router.push(`/manga?id=${mangaId}&chap=${++chapter}`)}>Next Chapter</button>
        {chapterPagesbase64.map((page)=>{
          return <img src={"data:image/png;base64,"+page} key={page}></img>
        })}
      </center>
    </div>
  )
}

export default Manga