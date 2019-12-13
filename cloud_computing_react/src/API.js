import axios from "axios";

export default axios.create({
  baseURL: "http://3.82.201.70/",
  responseType: "json"
});
