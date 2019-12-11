import axios from "axios";

export default axios.create({
  baseURL: "http://52.23.155.171/",
  responseType: "json"
});
