"use client";
import { cn } from "@/lib/utils";
import React from "react";
import { useState } from "react";
const Sidebar = () => {
  const [collapsed, setCollapsed] = useState(false);
  return (
    <aside
      className={cn(
        "transition-all duration-300",
        "h-[90%] bg-[#595168] z-10 self-end m-2 rounded-lg",
        collapsed ? "w-16" : "w-64"
      )}
    >
      <button onClick={() => setCollapsed(!collapsed)} className="p-2 text-5xl">
        -
      </button>
    </aside>
  );
};

export default Sidebar;
