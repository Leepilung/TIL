import axios from "axios";

export const getPost = (id) => axios.get(`https://picsum.photos/v2/list/${id}`);

export const getUsers = (id) => axios.get("https://picsum.photos/v2/list");
