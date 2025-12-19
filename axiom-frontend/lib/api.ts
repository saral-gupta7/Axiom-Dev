import axios from "axios";

const generateAxiom = async (prompt: string) => {
  const res = await axios.post("http://16.170.236.211:8000/run", { prompt });
  return res.data;
};

export default generateAxiom;
