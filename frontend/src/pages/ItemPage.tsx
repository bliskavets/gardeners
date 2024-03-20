import { Box, Text } from "@chakra-ui/react";
import { memo } from "react";
import { useParams } from "react-router-dom";

const ItemPage = () => {
  const itemId = useParams().itemId!;

  return (
    <Box>
      <Text>Item ID: {itemId}</Text>
    </Box>
  );
};

export default memo(ItemPage);
