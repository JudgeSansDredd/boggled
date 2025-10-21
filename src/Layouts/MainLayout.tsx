import React, { useEffect } from 'react';

interface PropType {
  pageName: string;
}

export default function MainLayout(props: React.PropsWithChildren<PropType>) {
  useEffect(() => {
    document.title = `Boggled | ${props.pageName}`;
  }, [props.pageName]);

  return (
    <>
      <div className="min-h-screen overflow-y-auto min-w-screen">
        <div className="container min-h-screen mx-auto">{props.children}</div>
      </div>
    </>
  );
}
