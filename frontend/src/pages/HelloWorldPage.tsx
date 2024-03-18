import { Box, Text } from '@chakra-ui/react';
import { memo } from "react";

const DemoPage = () => {
  return (
    <Box p={4}>
      <Text fontSize="xl">Hello World!!!</Text>
    </Box>
  );
};

export default memo(DemoPage);
