import React from "react";

const Navbar = () => {
  return (
    <article className="w-full h-20 relative z-3 bg-black">
      <div className="absolute inset-0 flex justify-end items-center p-10">
        <ul className="flex gap-5">
          <li>Home</li>
          <li>Contact</li>
        </ul>
      </div>
    </article>
  );
};

export default Navbar;
