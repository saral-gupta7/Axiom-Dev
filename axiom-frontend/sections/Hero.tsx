import React from "react";
import Header from "../components/Header";
import Navbar from "../components/Navbar";
import Searchbar from "../components/Searchbar";

const Hero = () => {
  return (
    <section className="h-dvh">
      <Navbar />
      <Header />
      <div className="w-full flex justify-center p-10">
        <Searchbar />
      </div>
    </section>
  );
};

export default Hero;
