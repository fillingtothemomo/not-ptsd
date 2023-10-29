"use client";
import React from 'react'
import { useRouter } from 'next/navigation'
import { useSearchParams } from 'next/navigation'
import "../../styles/manga.css";
function Manga() {
  const searchParams = useSearchParams()
  const router = useRouter()
  const mangaId  = searchParams.get("id");
  var chapter = parseInt(searchParams.get("chap")!)||1;
  const chapterPages= "wfw,egvjew,whevjywe,euhgkru"
  const chapterPagesbase64 = chapterPages.split(",")
  console.log(chapterPagesbase64);
  
  return (
    <div>
      <center>
        Manga Name: {mangaId} <br/>
        Chapter No: {chapter}<br />
        <button className='prev_button p-2' onClick={()=>router.push(`/manga?id=${mangaId}&chap=${--chapter}`)}>Previous Chapter</button>&nbsp;<button className='next_button p-2' onClick={()=>router.push(`/manga?id=${mangaId}&chap=${++chapter}`)}>Next Chapter</button>
        {chapterPagesbase64.map((page)=>{
          return <img src={page} key={page}></img>
        })}
      </center>
    </div>
  )
}

export default Manga