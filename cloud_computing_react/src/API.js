import axios from "axios";

export default axios.create({
  baseURL: "http://3.81.127.58/",
  responseType: "json"
});
