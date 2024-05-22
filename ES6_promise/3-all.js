/* eslint-disable */

import uploadPhoto from "./utils";
import CreateUser from "./utils";

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), CreateUser()])
    .then((values) =>
      console.log(
        `${values[0].body} ${values[1].firstName} ${values[1].lastName}`
      )
    )
    .catch(() => console.log("Signup system offline"));
}
