import { Router, Request, Response, NextFunction } from 'express';

const router = Router();

interface UserBody {
  name: string;
  email: string;
}

router.get('/', (_req: Request, res: Response) => {
  res.json([{ id: 1, name: '홍길동' }]);
});

router.get('/:id', (req: Request<{ id: string }>, res: Response) => {
  res.json({ id: req.params.id });
});

router.post('/', (req: Request<{}, {}, UserBody>, res: Response) => {
  res.status(201).json({ created: req.body });
});

router.put(
  '/:id',
  (req: Request<{ id: string }, {}, Partial<UserBody>>, res: Response) => {
    res.json({ updated: req.params.id, data: req.body });
  },
);

router.delete('/:id', (req: Request<{ id: string }>, res: Response) => {
  res.status(204).send();
});

export default router;
