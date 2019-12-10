import axios from "axios";

export default axios.create({
  baseURL: "http://18.232.94.219/",
  responseType: "json"
});
