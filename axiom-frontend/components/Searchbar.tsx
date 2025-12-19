import React, { useState } from "react";
import { cn } from "../lib/utils";
import { useMutation } from "@tanstack/react-query";
import generateAxiom from "../lib/api";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
const Searchbar = () => {
  const [prompt, setPrompt] = useState("");
  // const [error, setError] = useState("");
  // const [loading, setLoading] = useState(false);
  // const [data, setData] = useState(null);
  //
  const mutation = useMutation({ mutationFn: generateAxiom });

  // const handleGenerate = async () => {
  //   try {
  //     setLoading(true);
  //     setError("");

  //     const res = await generateAxiom(prompt);
  //     setData(res);
  //   } catch (error) {
  //     setError("Something went wrong");
  //   } finally {
  //     setLoading(false);
  //   }
  // };
  return (
    <div>
      <input
        type="text"
        placeholder="Let's generate your first axiom..."
        className={cn(
          "w-100 bg-white  p-5 rounded-xl rounded-r-none",
          "placeholder:text-black text-black"
        )}
        value={prompt}
        onChange={(e) => {
          setPrompt(e.target.value);
        }}
      />
      <button
        type="submit"
        className={cn("bg-white p-5 text-black font-bold", "rounded-r-xl")}
        onClick={() => {
          mutation.mutate(prompt);
        }}
        disabled={mutation.isPending}
      >
        Generate
      </button>

      <div>
        {mutation.isPending && <p>Generating...</p>}
        {mutation.isError && (
          <p className="text-red-500">Something went wrong!</p>
        )}
        {mutation.data?.plan && (
          <div className="bg-[#3B344A] p-5 rounded-lg">
            <p className="text-2xl font-bold">Plan:</p>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              rehypePlugins={[rehypeRaw]}
            >
              {mutation.data.plan.join("\n\n")}
            </ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  );
};

export default Searchbar;
