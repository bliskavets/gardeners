import { Box, Heading, Text } from "@chakra-ui/react";
import { memo, useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { apiFetch } from "../api";

const HelloWorldPage = () => {
  const [item, setItem] = useState(null);
  const [searchParams] = useSearchParams()
  const q = searchParams.get('q')

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await apiFetch({
          path: `/?q=${q}`,
        });
        setItem(data);
      } catch (error) {
        console.error("Fetching error:", error);
      }
    };

    fetchData();
  }, [q]);

  return (
    <Box>
      <Heading>Hello World!</Heading>
      <Text>Api call response: {JSON.stringify(item)}</Text>
    </Box>
  );
};

export default memo(HelloWorldPage);
