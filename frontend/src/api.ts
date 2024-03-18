import { createSearchParams } from "react-router-dom";

function stripUndefinedFileds(obj: Record<string, any>): Record<string, any> {
  const result: Record<string, any> = {};

  for (const key of Object.keys(obj)) {
    if (obj[key] !== undefined) {
      result[key] = obj[key];
    }
  }

  return result;
}

export async function apiFetch(
  options: RequestInit & {
    path: string;
    queryParams?: Record<
      string,
      string | string[] | boolean | number | undefined
    >;
  }
) {
  const response = await fetch(
    `http://0.0.0.0:8000/${options.path}?${createSearchParams(
      stripUndefinedFileds(options.queryParams || {})
    )}`,
    {
      method: options.method ?? "GET",
      ...options,
      headers: {
        "Content-Type": "application/json",
        ...options.headers,
      },
    }
  );

  console.debug(`fetching ${options.method ?? "GET"} ${options.path}`)

  if (!response.ok) {
    console.log(`responseBody: ${response.text}`)
    throw new Error(`api response is ${response.status}`);
  }

  const data = await response.json();
  return data
}
