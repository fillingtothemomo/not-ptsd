"use client";
import Image from "next/image";
import "../styles/home.css";
import {useRouter} from "next/navigation";
export default function Home() {
  const router = useRouter();
  const coverImage = "xyz,abc,erjk,wd,jnlw";
  const coverImageArray = coverImage.split(",");
  console.log(coverImageArray);
  return (
    <main>
      <div style={{ color: "red" }} className="h1">
        Manga Maestro
      </div>{" "}
      {coverImageArray.map((coverImage) => {
        return <img key={coverImage} src={coverImage} onClick={()=>router.push("/manga?id="+coverImage)}></img>;
      })}
    </main>
  );
}
