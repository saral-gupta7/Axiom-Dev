import api from "./api";

const generateAxiom = async (prompt: string) => {
  const res = await api.post("/run", { prompt });
  return res.data;
};

export default generateAxiom;
