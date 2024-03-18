// eslint-disable-next-line no-restricted-imports
import { memo } from "react";
import AppRouter from "./AppRouter";

export function App() {
  return <AppRouter />;
}

export default memo(App);
